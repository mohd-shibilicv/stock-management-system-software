import React from "react";
import { useLocation, Link } from "react-router-dom";
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip";
import {
  Bell,
  LayoutDashboard,
  PackageSearch,
  Truck,
  Warehouse,
  ArrowDownToDot,
  ArrowUpFromDot,
  Layers3,
  Container,
  HeartCrack,
  PhoneIncoming,
} from "lucide-react";
import LogoutBtn from "./LogoutBtn";

const StoreSidebar = () => {
  const location = useLocation();

  const isActive = (path) => {
    return location.pathname === path
      ? "bg-black text-white"
      : "hover:bg-gray-100";
  };

  const menuItems = [
    { path: "/store", icon: LayoutDashboard, label: "Dashboard" },
    { path: "/store/products", icon: PackageSearch, label: "Products" },
    { path: "/store/suppliers", icon: Truck, label: "Suppliers" },
    { path: "/store/branches", icon: Warehouse, label: "Branches" },
    {
      path: "/store/damaged-products",
      icon: HeartCrack,
      label: "Damaged Products",
    },
    {
      path: "/store/product-requests",
      icon: PhoneIncoming,
      label: "Product Requests",
    },
    {
      path: "/store/product-inflow",
      icon: ArrowDownToDot,
      label: "Product Inflows",
    },
    {
      path: "/store/product-outflow",
      icon: ArrowUpFromDot,
      label: "Product Outflows",
    },
    { path: "/store/reports", icon: Layers3, label: "Reports" },
  ];

  const renderMenuItem = (item) => (
    <TooltipProvider key={item.path}>
      <Tooltip>
        <TooltipTrigger asChild>
          <Link
            to={item.path}
            className={`flex items-center space-x-2 p-2 rounded ${isActive(
              item.path
            )}`}
          >
            <item.icon className="w-6 h-6" />
            <span className="hidden md:inline">{item.label}</span>
          </Link>
        </TooltipTrigger>
        <TooltipContent side="right" className="md:hidden">
          <p>{item.label}</p>
        </TooltipContent>
      </Tooltip>
    </TooltipProvider>
  );

  return (
    <div className="w-20 md:w-64 bg-white p-4 h-screen border-r border-gray-300 flex flex-col">
      <Link to="/" className="mb-8 flex justify-center md:justify-start">
        <div className="hidden sm:block text-black-500 text-2xl font-bold">
          InventoryPro
        </div>
        <div className="block sm:hidden text-black-500 text-2xl font-bold">
          <Container />
        </div>
      </Link>
      <nav className="flex-grow">
        <ul className="space-y-2">{menuItems.map(renderMenuItem)}</ul>
      </nav>
      <div className="mt-8">
        <ul>
          <TooltipProvider>
            <Tooltip>
              <TooltipTrigger asChild>
                <Link
                  to="/store/notifications"
                  className={`flex items-center space-x-2 p-2 rounded ${isActive(
                    "/store/notifications"
                  )}`}
                >
                  <Bell className="w-6 h-6" />
                  <span className="hidden md:inline">Notifications</span>
                </Link>
              </TooltipTrigger>
              <TooltipContent side="right" className="md:hidden">
                <p>Notifications</p>
              </TooltipContent>
            </Tooltip>
          </TooltipProvider>
          <LogoutBtn />
        </ul>
      </div>
    </div>
  );
};

export default StoreSidebar;
