import React, { useState, useContext, useEffect } from 'react'
import { getIndex } from '../utils/apiCalls'
import { Context as nameContext } from '../utils/handleName'

// const { name, setName } = useContext(nameContext)

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
