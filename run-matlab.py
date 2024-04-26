import matlab.engine

# Start MATLAB engine
eng = matlab.engine.start_matlab()

# Call your MATLAB function
func_num = matlab.double([3]) 
n = matlab.double([10]) 

eng.main(func_num, n, nargout=0)

# Close MATLAB engine
eng.quit()