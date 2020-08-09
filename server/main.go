package main
import (
  "encoding/json"
  "go-py-gRPC/server/countries" //compiled package proto for golang
  "io/ioutil"
  "log"
  "net"
  "net/http"
  "golang.org/x/net/context"
  "google.golang.org/grpc"
)
func main() {
  //creating a gRPC server
  grpcServer := grpc.NewServer()

  //GO server
  var server Server

  //connecting or regitering our GO server to gRPC server

  countries.RegisterCountryServer(grpcServer, server)
  listen, err := net.Listen("tcp", "0.0.0.0:3001")
  if err != nil {
    log.Fatalf("could not listen to 0.0.0.0:3001 %v", err)
  }
  log.Println("Server is Running @3001")
  log.Fatal(grpcServer.Serve(listen))
}


//GO server
type Server struct{}

func (Server) Search(ctx context.Context, request *countries.CountryRequest) (*countries.CountryResponse, error) {
  resp, err := http.Get("https://restcountries.eu/rest/v2/name/ " + request.Name)
  if err != nil {
    return nil, err
  }
  defer resp.Body.Close()
  jsonData, err := ioutil.ReadAll(resp.Body)
  if err != nil {
    return nil, err
  }
  var data []countries.CountryResponse
  if err := json.Unmarshal(jsonData, &data); err != nil {
    return nil, err
  }
  return &data[0], nil
}