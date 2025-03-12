import React, {useEffect, useState} from 'react'
import axios, { AxiosResponse } from 'axios'
import '../cssFiles/home.css'
import { json } from 'express'

const URL = 'http://localhost:5000'

const Home = () => {
  const [jsonData, setJsonData] = useState<String[] | null>(null)
  const [resData, setResData] = useState<AxiosResponse | null> (null)

  const fetchDataFromLogisticRegression = async () => {
    await axios.post(URL + `/logisticRegression/${{jsonData}}`)
    .then((response) => {
      setResData(response.data)
    })
    .catch((error) => {
      console.log(error)
    })
    
  }

  
  const convertCSVToJson = (csvData: any) => {
    const lines: String[] = csvData.split("\n")

    const headers = lines[0].split(",")
    const result = []

    for (let i = 1; i < lines.length; i++) {
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
    <div className='center-container'>
      <div className='white-opaciity-box'>
        <input type="file" accept='.csv' onChange={handleChange}/>
        <h3>{resData? JSON.stringify(resData) : 'Please enter CSV file'}</h3>
      </div>
    </div>
  )
}

export default Home
