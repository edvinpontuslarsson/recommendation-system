const host = process.env.REACT_APP_API_HOST || 'http://localhost'
const port = process.env.REACT_APP_API_PORT || 4433
const apiUrl = `${host}:${port}/api`

const getPostObj = bodyObj => {
  return {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(bodyObj)
  }
}

export const postIndex = async name => {
  const response = await fetch(apiUrl, getPostObj({ name }))

  return response.json()
}
