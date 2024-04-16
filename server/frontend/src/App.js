
import Register from "./components/Register/Register"
import RootPage from "./components/RootPage"; // Import your RootPage component
import LoginPanel from "./components/Login/Login"
import LogoutPage from "./components/LogoutPage";
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPanel />} />
      <Route path="/root" element={<RootPage />} />
      <Route path="/logout" element={<LogoutPage />} />
      <Route path='/register' element={<Register/>} />
    </Routes>
  );
}

export default App;
