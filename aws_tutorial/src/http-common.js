import axios from "axios";

export default axios.create({
  baseURL:
  "http://localhost:8000/", // for local development

  headers: {
    'Content-Type': 'multipart/form-data' ,   
    "Access-Control-Allow-Origin": "*",
  },
});