const host = process.env.REACT_APP_API_HOST || 'http://localhost'
const port = process.env.REACT_APP_API_PORT || 4433
const apiUrl = `${host}:${port}/api`

export const getIndex = async () => {
  const response = await fetch(apiUrl)
  return response.json()
}
