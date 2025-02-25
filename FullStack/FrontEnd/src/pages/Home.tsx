import { useState } from "react"
// import * as fs from "fs"

const Home = () => {

  const [jsonData, setJsonData] = useState<Object[] | null>(null)

  // const writeJsonFile = () => {

  //   console.log("Wirte json file");
  //   try {
  //     fs.writeFileSync("jsonFile", JSON.stringify(jsonData, null, 2))
  //   } catch (e) {
  //     console.log(e);
      
  //   }
  // }

  const convertCSVToJson = (csvData: any) => {
    const lines: String[] = csvData.split("\n")

    const headers = lines[0].split(",")     
    const result = []

    for (let i = 1; i < lines.length; i++) {
        const obj = {} as any
        const currentLine: String[] = lines[i].split(",")        

        for (let j = 0; j < headers.length; j++) {
            obj[headers[j]] = currentLine[j]
        }

        result.push(obj)
    }
    return result
  }

  const HandleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if(e.target.files) {
        const file = e.target.files[0];
        const reader = new FileReader();
        
        reader.onload = (e) => {
            const csvData = e.target?.result
            
            const jsonData = convertCSVToJson(csvData)
            setJsonData(jsonData)
        }

        reader.readAsText(file)

        writeJsonFile()
    }
    
  }

  return (
    <div>
      <input type="file" accept=".csv" onChange={HandleInputChange}/>

      {jsonData ? (<div>{JSON.stringify(jsonData, null, 2)}</div>) : 
      (
        <p>Please select a CSV file</p>
      )}
    </div>
  )
}

export default Home
