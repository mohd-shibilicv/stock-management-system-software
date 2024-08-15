import { isTokenExpired } from '@/lib/isTokenExpired';
import { login, logout, refreshToken as refreshTokenAPI } from '@/services/api';
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';

export const loginUser = createAsyncThunk(
  'auth/login',
  async (credentials, { rejectWithValue }) => {
    try {
      const response = await login(credentials);
      return response;
    } catch (error) {
      return rejectWithValue(error.response?.data?.detail || 'An error occurred');
    }
  }
);

export const logoutUser = createAsyncThunk(
  'auth/logout',
  async (_, { getState, rejectWithValue }) => {
    try {
      const { refreshToken, token } = getState().auth;
      if (token) {
        await logout({ refresh_token: refreshToken });
      }
      localStorage.removeItem('token');
      localStorage.removeItem('refresh');
    } catch (error) {
      return rejectWithValue(error.response?.data || 'An error occurred');
    }
  }
);

export const refreshAccessToken = createAsyncThunk(
  'auth/refreshToken',
  async (_, { getState, dispatch }) => {
    const { refreshToken } = getState().auth;
    try {
      const data = await refreshTokenAPI(refreshToken);
      return data;
    } catch (error) {
      dispatch(logoutUser());
      throw error;
    }
  }
);

export const tokenMiddleware = ({ dispatch, getState }) => next => async action => {
  if (action.type !== 'auth/refreshToken' && typeof action === 'function') {
    const { auth } = getState();
    if (auth.token && isTokenExpired(auth.token)) {
      if (!isTokenExpired(auth.refreshToken)) {
        await dispatch(refreshAccessToken());
      } else {
        dispatch(logoutUser());
        return;
      }
    }
  }
  return next(action);
};

const authSlice = createSlice({
  name: 'auth',
  initialState: {
    user: null,
    token: null,
    refreshToken: null,
    isLoading: false,
    error: null,
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(loginUser.pending, (state) => {
        state.isLoading = true;
        state.error = null;
      })
      .addCase(loginUser.fulfilled, (state, action) => {
        state.isLoading = false;
        state.user = action.payload.user;
        state.token = action.payload.access;
        state.refreshToken = action.payload.refresh;
      })
      .addCase(loginUser.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.payload;
      })
      .addCase(logoutUser.pending, (state) => {
        state.isLoading = true;
      })
      .addCase(logoutUser.fulfilled, (state) => {
        state.user = null;
        state.token = null;
        state.refreshToken = null;
        state.isLoading = false;
      })
      .addCase(logoutUser.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.payload;
      })
      .addCase(refreshAccessToken.fulfilled, (state, action) => {
        state.token = action.payload.access;
        if (action.payload.refresh) {
          state.refreshToken = action.payload.refresh;
        }
      });
  },
});

export default authSlice.reducer;
