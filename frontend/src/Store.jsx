import "./App.css";
import { Routes, Route } from "react-router-dom";
import StoreDashboardPage from "./pages/storePages/StoreDashboardPage";
import NotFound404 from "./components/layout/NotFound404";
import StoreProducts from "./pages/storePages/StoreProducts";
import Suppliers from "./pages/storePages/Suppliers";
import Branches from "./pages/storePages/Branches";
import ProductInflow from "./pages/storePages/ProductInflow";
import ProductOutflow from "./pages/storePages/ProductOutflow";
import StoreReports from "./pages/storePages/StoreReports";
import Notifications from "./pages/storePages/Notifications";

function Store() {
  return (
    <>
      <Routes>
        <Route path="/" element={<StoreDashboardPage /> } />
        <Route path="/products" element={<StoreProducts /> } />
        <Route path="/suppliers" element={<Suppliers /> } />
        <Route path="/branches" element={<Branches /> } />
        <Route path="/product-inflow" element={<ProductInflow /> } />
        <Route path="/product-outflow" element={<ProductOutflow /> } />
        <Route path="/reports" element={<StoreReports /> } />
        <Route path="/notifications" element={<Notifications /> } />
        <Route path="*" element={<NotFound404 /> } />
      </Routes>
    </>
  );
}

export default Store;
