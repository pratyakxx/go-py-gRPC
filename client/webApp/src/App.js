import React, {useState,useEffect} from 'react';
import 'antd/dist/antd.css';
import './App.css';
import Status from "./components/Search"
import Details from "./components/Details"
import axios from 'axios';
import { Input } from 'antd';
const { Search } = Input;

const App = () =>  {

  const [connected, setConnected] = useState(false)
  const [data, setData] = useState({})
  const [error, setError] = useState(false)
  const [country, setCountry] = useState("")

  useEffect(() => {
    axios.get(`http://localhost:5000/${country}`)
    .then((res)=>{
      console.log(res.data)
      setData(res.data)
      setError(false)
    })
    .catch((error)=>{
      console.error(error)
      setError(true)
  })

  axios.get("http://localhost:5000/germany")
    .then((res)=>{
      setConnected(true)
    })
    .catch((error)=>{
  })
  },[country])


  return (
    <div className="App">
      <div className="title">GO-PYHTON-GRPC</div>
      <div className="status">{ connected ? <Status connected={true}/> : <Status connected={false}/> }</div>
      <div className="SearchBar">
          <Search
          placeholder="Enter the Country.... "
          enterButton="Search"
          size="large"
          onSearch={value => setCountry(value)}
          style={{ width: 500 }}
          />
      </div>
      <div>
        {country ? error ? "Country data not avilable": <Details data={data}/> : "Please enter the country for details"}
      </div>


    </div>
  );
}

export default App;
