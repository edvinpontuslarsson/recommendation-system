import React, { useState, useEffect } from 'react'
import { getIndex } from '../utils/apiCalls'

const Welcome = () => {
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

export default Welcome
