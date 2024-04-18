//import RootPage from "./components/RootPage"; // Import your RootPage component
import { Routes, Route } from "react-router-dom";
import LoginPanel from "./components/Login/Login";
import Register from "./components/Register/Register";
import LogoutPage from "./components/LogoutPage";


function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPanel />} />
      
      <Route path="/logout" element={<LogoutPage />} />
      <Route path='/register' element={<Register/>} />
    </Routes>
  );
}

export default App;
//<Route path="/root" element={<RootPage />} />