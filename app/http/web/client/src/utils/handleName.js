import React, { createContext, useState } from 'react'

export const Context = createContext({})

export const Provider = props => {
  const [name, setName] = useState('')

  const clearName = () => {
    setName('')
  }

  const nameContext = {
    name,
    setName,
    clearName
  }

  return (
    <Context.Provider value={nameContext}>{props.children}</Context.Provider>
  )
}
