import { useState, useEffect } from 'react';
import NavBar from './components/NavBar';
import Preloader from './components/Preloader';
import FooterSection from './components/FooterSection';
import HomePage from './pages/HomePage'
import Header from './components/Header/Header';
import { BrowserRouter, Routes, Route } from "react-router-dom";


function App() {

  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const timer = setTimeout(() => {
      setIsLoading(false);
    }, 2000);

    return () => clearTimeout(timer);
  }, []);
  
  return (
    <>
      {isLoading ? (
        <Preloader />
      ) : (
          <>
          <BrowserRouter>
            <Header /> {/* Header component contains <Link> */}
            <Routes>
              <Route path="/" element={<HomePage />} />
              {/* <Route path="/about" element={<AboutPage />} /> */}
            </Routes>
          </BrowserRouter>
            {/* <Header/>
            <NavBar />
            <HomePage />
            <FooterSection /> */}
          </>
      )}
    </>
  )
}

export default App
