# the reverse operation - Converting None to NaN in numpy when casting a list to numpy arrays

u = np.where(np.isnan(y), None, y).tolist()
