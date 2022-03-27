import './App.css';
import CreatePhrase from './create_phrase'
import { useState, useEffect } from 'react';

function App() {
    const [initialData, setInitialData] = useState([{}])

    useEffect(()=> {
      fetch('/api').then(
        response => response.json()
      ).then(data => setInitialData(data))
    }, []);
    // return (
    //   <div className="App">
    //      <CreatePhrase />
    //   </div>
    // );
    return(
      <div>
          <ol>
          {
              useEffect.data.map(data => (
                  <li key={data.id} align="start">
                      <div>
                          <p>{data.username}</p>
                          <p>{data.password}</p>
                      </div>
                  </li>
              ))
          }
          </ol>
      </div>
  );
}

export default App
