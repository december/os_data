va_list = [0xc2265b1f, 0xcc386bbc, 0xc7ed4d57, 0xca6cecc0, 0xc18072e8, \
			0xcd5f4b3a, 0xcc324c99, 0xc7204e52, 0xc3a90293, 0xce6c3f32]
pa_list = [0x0d8f1b1f, 0x0414cbbc, 0x07311d57, 0x0c9e9cc0, 0x007412e8, \
			0x06ec9b3a, 0x0008ac99, 0x0b8b6e52, 0x0f1fd293, 0x007d4f32]
count = 0
while (count < 10):
	pde_idx = va_list[count] >> 22
	pde_ctx = ((pde_idx - 0x300 + 1) << 12) + 0x003
	pte_idx = (va_list[count] >> 12) & 0x3FF
	pte_ctx = ((pa_list[count] >> 12) << 12) + 0x003
	print 'va 0x%08x, pa 0x%08x, pde_idx 0x%08x, pde_ctx 0x%08x, pte_idx 0x%08x, pte_ctx 0x%08x' \
	% (va_list[count], pa_list[count], pde_idx, pde_ctx, pte_idx, pte_ctx)
	count = count + 1

print 'End'
