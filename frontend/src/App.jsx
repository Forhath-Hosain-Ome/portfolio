import "@fancyapps/ui/dist/fancybox/fancybox.css";
import { useState, useEffect } from 'react';
import RouterLinks from "./router/Routes.jsx";
import { HelmetProvider } from 'react-helmet-async'

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
        <HelmetProvider>
          <RouterLinks></RouterLinks>
        </HelmetProvider>
      )}
    </>
  )
}

export default App
