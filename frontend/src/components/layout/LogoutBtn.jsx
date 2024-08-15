import { logoutUser } from "@/features/slices/authSlice";
import { LogOutIcon } from "lucide-react";
import React from "react";
import { useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";

const LogoutBtn = () => {
  const navigate = useNavigate();
  const dispatch = useDispatch();

  const handleLogout = async () => {
    try {
      await dispatch(logoutUser()).unwrap();
      navigate("/login");
    } catch (error) {
      console.error(`Failed to log out: ${error}`);
    }
  };

  return (
    <button
      className="w-full flex items-center space-x-2 px-3 hover:text-red-500 cursor-pointer mt-2 justify-start py-1 rounded-md focus:outline-none"
      onClick={handleLogout}
    >
      <LogOutIcon />
      <p className="hidden sm:block">Logout</p>
    </button>
  );
};

export default LogoutBtn;