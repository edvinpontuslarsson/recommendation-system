import React, { useState, useEffect } from 'react'
import './App.css'
import { getIndex } from './lib/apiCalls'

const App = () => {
  const [message, setMessage] = useState('')

  useEffect(() => {
    if (!message) {
      fetchMessage()
    }
  }, [])

  const fetchMessage = async () => {
    const payload = await getIndex()
    setMessage(payload.message)
  }

  return (
    <>
      <h1>{message}</h1>
    </>
  )
}

export default App
