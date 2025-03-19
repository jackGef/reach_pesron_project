import React, {useEffect, useState} from 'react'
import axios, { AxiosResponse } from 'axios'
import './home.css'
import Header from '../components/Header';
import Plot from 'react-plotly.js'

const URL = 'http://192.168.165.55:5000'

const Home = () => {
  const [jsonData, setJsonData] = useState<String[] | null>(null)
  const [resData, setResData] = useState<AxiosResponse | null> (null)

  const fetchDataFromLogisticRegression = async () => {

    console.log("Sending JSON Data:", jsonData);
  
    try {
      const response = await axios.post(URL + "/logisticRegression", jsonData, {
        headers: { "Content-Type": "application/json" }
      });
      setResData(response.data);
    } catch (error) {
      console.error("Error sending data:", error);
    }
  };

  
  const convertCSVToJson = (csvData: any) => {
    const lines: String[] = csvData.split("\n")

    const headers = lines[0].split(",")
    const result = []

    for (let i: number = 1; i < lines.length; i++) {
      const obj: any = {}
      const currentLine: String[] = lines[i].split(",")

      for (let j = 0; j < headers.length; j++) {
        obj[headers[j]] = currentLine[j]
      }

      result.push(obj)
    }

    return result
  }

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) {
      const file = e.target.files[0]
      const reader = new FileReader()

      reader.onload = (e) => {
        const csvData = e.target?.result

        const jsonRes = convertCSVToJson(csvData)
        setJsonData(jsonRes)        
      }

      reader.readAsText(file)            
    }
  }

  useEffect(() => {
    fetchDataFromLogisticRegression()
  }, [jsonData])

  return (
    <div>
      <Header/>
      <div className='main-container'>
        <div className='white-opaciity-box'>
          <input type="file" accept='.csv' onChange={handleChange}/>
          <h3>{resData? JSON.stringify(resData) : 'Please enter CSV file'}</h3>
        </div>
          <Plot
            data={[
              {
                z: [[1, null, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -10, 20]],
                x: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                y: ['Morning', 'Afternoon', 'Evening'],
                type: 'heatmap',
                hoverongaps: false
              },
            ]}

            layout={ {width: 700, height: 620, paper_bgcolor: "rgb(0, 0, 0, 0.6)", title: {text: 'A Fancy Plot'}} }
            />
      </div>
    </div>
  )
}

export default Home
