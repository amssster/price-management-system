import { configureStore } from '@reduxjs/toolkit';
import importReducer from './importSlice';
import productReducer from './productSlice';
import supplierReducer from './supplierSlice';

export const store = configureStore({
  reducer: {
    imports: importReducer,
    products: productReducer,
    suppliers: supplierReducer,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
