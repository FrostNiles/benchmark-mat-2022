import matlab.engine

# Start MATLAB engine
eng = matlab.engine.start_matlab()

# Call your MATLAB function
func_num = 2
n = 10

eng.main(func_num, n, nargout=0)

# Close MATLAB engine
eng.quit()