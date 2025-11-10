import { useState, useEffect } from 'react';
import NavBar from './components/NavBar';
import Preloader from './components/Preloader';
import FooterSection from './components/FooterSection';
import HomePage from './pages/HomePage'


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
            <NavBar />
            <HomePage />
            <FooterSection />
          </>
      )}
    </>
  )
}

export default App
