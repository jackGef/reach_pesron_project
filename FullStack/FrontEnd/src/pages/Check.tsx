import axios from 'axios'
import React, {useState, useEffect} from 'react'

const Check = () => {
    const [array, setArray] = useState([])

    const fetchAPI = async () => {
        const response = await axios.get("http://localhost:5000/api/users")
        console.log(response.data.users);
        
        setArray(response.data.users)
    }

    const fetchUser = async () => {
        const response = await axios.post(`http://localhost:5000/api/users/jack/Hello`, {"user": "Jackob"})
        console.log(response.data);
    }

    useEffect(() => {
        // fetchAPI()
        fetchUser()
    }, [])

  return (
    <div>
      {
        array.map((user, index) => (
            <div key={index}>
                <span>{user}</span>
                <br></br>
            </div>  
        ))
      }
    </div>
  )
}

export default Check
