import React, { useState } from 'react'
import { postIndex } from '../utils/apiCalls'

const BasicForm = () => {
  const [name, setName] = useState('')
  const [message, setMessage] = useState('')

  const handleChange = event => {
    setName(event.target.value)
  }

  const handleSubmit = event => {
    fetchMessage()
    event.preventDefault()
  }

  const fetchMessage = async () => {
    try {
      const payload = await postIndex(name)
      setMessage(payload.message)
    } catch (error) {
      setMessage('Something went wrong')
      console.error(error)
    }
  }

  return (
    <>
      <form onSubmit={handleSubmit}>
        <label>Enter your name: </label>
        <input type="text" onChange={handleChange} />
      </form>

      <p>
        <b>{message}</b>
      </p>
    </>
  )
}

export default BasicForm
