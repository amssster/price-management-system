import { createSlice, PayloadAction } from '@reduxjs/toolkit';

// Слайс для поставщиков
const supplierSlice = createSlice({
  name: 'suppliers',
  initialState: [] as any[],
  reducers: {},
});

export default supplierSlice.reducer;
