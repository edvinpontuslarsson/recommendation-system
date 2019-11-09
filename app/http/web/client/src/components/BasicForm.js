import React, { useState, useEffect } from 'react'

/**
 * const [message, setMessage] = useState('')

  useEffect(() => {
    if (!message) {
      fetchMessage()
    }
  }, [])

  const fetchMessage = async () => {
    const payload = await getIndex()
    setMessage(payload.message)
  }
 */

// Todo: have separate state file for welcome,
// can change based on form here
// but fix in server first

// maybe I can do pr on this now, nah fix in server

const BasicForm = () => {
  return (
    <>
      <form>
        <input type="text" onSubmit={} />
        {/** Todo: do I need btn here? */}
      </form>
    </>
  )
}

export default BasicForm
