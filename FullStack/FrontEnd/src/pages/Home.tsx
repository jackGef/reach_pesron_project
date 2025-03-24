import React, {useEffect, useState} from 'react'
import axios, { AxiosResponse } from 'axios'
import './home.css'
import Header from '../components/Header';
import Plot from 'react-plotly.js'

const URL = 'http://192.168.111.79:5000'

const Home = () => {

  const [jsonData, setJsonData] = useState<String[] | null>(null)
  const [resData, setResData] = useState<resStructure | null> (null)

  interface resStructure {
    Accuracy: number;
    Y_predictions: {
      Y_true_positive: number,
      Y_true_negative: number,
      Y_false_positive: number,
      Y_false_negative: number,
    },
    loss: number[]
  }

  const fetchDataFromLogisticRegression = async () => {

    console.log("Sending JSON Data:", jsonData);
  
    try {
      const response = await axios.post(URL + "/logisticRegression", jsonData, {
        headers: { "Content-Type": "application/json" }
      });
      setResData(response.data);
      console.log(resData);
      // console.log(response.data);
      
      
    } catch (error) {
      console.error("Error sending data:", error);
    }
  };

  
  const convertCSVToJson = (csvData: string) => {
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

        const jsonRes = convertCSVToJson(csvData as string)
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
          <Plot
            data={[
              {
                z: [[
                  resData?.Y_predictions?.Y_true_positive ?? 0, 
                  resData?.Y_predictions?.Y_true_negative ?? 0
                ],
                [
                  resData?.Y_predictions?.Y_false_negative ?? 0,
                  resData?.Y_predictions?.Y_false_positive ?? 0
                ]],
                x: ['Positive', 'Negative'],
                y: ['True', 'False'],
                type: 'heatmap',
                hoverongaps: false
              },
            ]}
            
            layout={ {width: 700, height: 620, paper_bgcolor: "rgb(0, 0, 0, 0.6)", title: {text: 'A Fancy Plot'}} }
            />
        </div>
          {resData===null? "Please enter something": JSON.stringify(resData.Accuracy)}
      </div>
    </div>
  )
}

export default Home
