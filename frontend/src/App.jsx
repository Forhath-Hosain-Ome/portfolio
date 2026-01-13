// import { useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
// import './App.css'
import "@fancyapps/ui/dist/fancybox/fancybox.css";

// function App() {
//   const [count, setCount] = useState(0)

//   return (
//     <>
//       <div>
//         <a href="https://vitejs.dev" target="_blank">
//           <img src={viteLogo} className="logo" alt="Vite logo" />
//         </a>
//         <a href="https://react.dev" target="_blank">
//           <img src={reactLogo} className="logo react" alt="React logo" />
//         </a>
//       </div>
//       <h1>Vite + React</h1>
//       <div className="card">
//         <button onClick={() => setCount((count) => count + 1)}>
//           count is {count}
//         </button>
//         <p>
//           Edit <code>src/App.jsx</code> and save to test HMR
//         </p>
//       </div>
//       <p className="read-the-docs">
//         Click on the Vite and React logos to learn more
//       </p>
//     </>
//   )
// }

// export default App
import { useState, useEffect } from 'react';
import RouterLinks from "./router/Routes.jsx";
// import { PushSpinner  } from "react-spinners";
import { 
  CircleLoader,
  ClipLoader, 
  PulseLoader,
  BeatLoader,
  BarLoader,
  DotLoader,
  RingLoader,
  ScaleLoader
} from "react-spinners";


function App() {
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    setLoading(true);
    setTimeout(() => {
      setLoading(false);
    }, 2000);
  }, []);
  
  return (
    <>
      {loading ? (
        <div className="pageLoader fixed justify-center items-center inset-0 flex">
          <PulseLoader 
            className="bg-accent"
            size={60}
            color="#284be5"
          ></PulseLoader>
        </div>
      ) : (
        <RouterLinks></RouterLinks>
      )}
    </>
  )
}

export default App
