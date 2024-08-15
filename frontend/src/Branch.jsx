import "./App.css";
import { Routes, Route } from "react-router-dom";
import BranchDashboardPage from "./pages/branchPages/BranchDashboardPage";
import InventoryPage from "./pages/branchPages/InventoryPage";
import ProductRequestsPage from "./pages/branchPages/ProductRequestsPage";
import ReportsPage from "./pages/branchPages/ReportsPage";
import ProfilePage from "./pages/branchPages/ProfilePage";
import NotificationPage from "./pages/branchPages/NotificationPage";

function Branch() {
  return (
    <>
      <Routes>
        <Route path="/" element={<BranchDashboardPage />} />
        <Route path="/inventory" element={<InventoryPage />} />
        <Route path="/requests" element={<ProductRequestsPage />} />
        <Route path="/reports" element={<ReportsPage />} />
        <Route path="/profile" element={<ProfilePage />} />
        <Route path="/notifications" element={<NotificationPage />} />
      </Routes>
    </>
  );
}

export default Branch;
