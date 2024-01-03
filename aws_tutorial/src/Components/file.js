import React from 'react'
import { useEffect, useCallback } from 'react'
import fileService from './fileService'
import {useDropzone} from 'react-dropzone'


function File() {

  const onDrop = useCallback(acceptedFiles => {
    console.log(acceptedFiles)

    const formData = new FormData()
    formData.append('file', acceptedFiles[0])

    fileService.uploadFile(formData)
      .then(response => {
        console.log(response)
      })
      .catch(error => {
        console.log(error)
      })


  }, [])

  const {getRootProps, getInputProps, isDragActive} = useDropzone({onDrop})

  const [file, setFile] = React.useState(null)

  useEffect(() => {
      fetchAllFiles()
    }, [])

const fetchAllFiles = ()=>{
    fileService
    .getAllFiles()
    .then((response)=>{
        console.log(response.data)
    }).catch((error)=>{
        console.log(error)
    })
    }
    


  return (
    <div className='mx-auto w-full p-3 rounded-3xl  '>
      <div {...getRootProps()} className='bg-slate-300 h-96 rounded-2xl text-center flex justify-center items-center'>
      <input {...getInputProps()} />
      {
        isDragActive ?
          <h1 className='text-2xl'>Drop the files here ...</h1> :
          <h1 className='text-2xl'>Drag 'n' drop some files here, or click to select files</h1>
      }
    </div>

    <div className='mt-8'>
      <h1 className='text-2xl text-white'>  Files in AWS database</h1>
    </div>

    </div>
  )
}

export default File