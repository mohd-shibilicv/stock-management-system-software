import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Provider } from 'react-redux';
import { store } from "./features/store";
import Branch from "./Branch";
import Store from "./Store";
import LoginPage from "./pages/generals/LoginPage";
import NotFound404 from "./components/layout/NotFound404";
import { BranchProtectedRoute } from "./components/layout/BranchProtectedRoute";
import { AuthenticatedRoute, StoreProtectedRoute } from "./components/layout/StoreProtectedRoute";
import GeneralViewPage from "./pages/generals/GeneralViewPage";
import Unauthorized from "./components/layout/Unauthorized";

function App() {
  return (
    <Provider store={store}>
      <Router>
        <Routes>
          <Route path="/login" element={<AuthenticatedRoute><LoginPage /></AuthenticatedRoute>} />
          <Route path="/" element={<GeneralViewPage />} />
          <Route
            path="/branch/*"
            element={
              <BranchProtectedRoute allowedRoles={['branch_manager']}>
                <Branch />
              </BranchProtectedRoute>
            }
          />
          <Route
            path="/store/*"
            element={
              <StoreProtectedRoute allowedRoles={['admin']}>
                <Store />
              </StoreProtectedRoute>
            }
          />
          <Route path="/unauthorized" element={<Unauthorized />} />
          <Route path="*" element={<NotFound404 />} />
        </Routes>
      </Router>
    </Provider>
  );
}

export default App;
