import { logoutUser } from '@/features/slices/authSlice';
import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useNavigate } from 'react-router-dom';

const TokenExpirationModal = () => {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const isTokenExpired = useSelector(state => state.auth.isTokenExpired);

  const handleLogout = async () => {
    try {
      await dispatch(logoutUser()).unwrap();
      navigate("/login");
    } catch (error) {
      console.error(`Failed to log out: ${error}`);
    }
  };

  if (!isTokenExpired) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
      <div className="bg-white p-6 rounded-lg">
        <h2 className="text-xl font-bold mb-4">Session Expired</h2>
        <p className="mb-4">Your session has expired. Please log in again to continue.</p>
        <button 
          onClick={handleLogout}
          className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
        >
          Log Out
        </button>
      </div>
    </div>
  );
};

export default TokenExpirationModal;