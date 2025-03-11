import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Login from './views/pages/Login/Login';
import { AuthProvider } from './context/AuthContext';
// import PrivateRoute from './views/components/Wrappers/PrivateRoute';
import MapPlanner from './views/pages/MapPlanner/MapPlanner';

function App() {
  return (
    // <AuthProvider>
      <Router>
        <Routes>
         <Route path="/login" element={<Login />} />
          <Route path="/" element={
            // <PrivateRoute>
              <MapPlanner />
            //  </PrivateRoute> 
          } />
        </Routes>
      </Router>
    // </AuthProvider>
  );
}

export default App;
