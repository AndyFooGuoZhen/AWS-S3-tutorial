import httpClient from  '../http-common'

const getAllFiles =()=>{
    return httpClient.get("/getFiles");
}

const uploadFile = (file)=>{
    return httpClient.post("/uploadFile",file);
}

export default {getAllFiles, uploadFile};