import { createSlice, PayloadAction } from '@reduxjs/toolkit';

// Слайс для товаров
const productSlice = createSlice({
  name: 'products',
  initialState: [] as any[],
  reducers: {},
});

export default productSlice.reducer;
