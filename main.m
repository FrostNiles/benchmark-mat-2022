function main(func_num, n)
    if nargin < 2
        func_num = 1;
        n = 10;
    end


    fprintf('func_num = %d, n = %d\n', func_num, n);
    m = 2;
    x = zeros(m*n, 1);
    f = zeros(m, 1);

    for i = func_num:func_num
        FileName = sprintf('test_data/shift_data_%d.txt', func_num);
        if exist(FileName, 'file') ~= 2
            error('Error: Cannot open input file for reading');
        end

        fileID = fopen(FileName,'r');
        x(1:n) = fscanf(fileID, '%f', [1, n]);
        fclose(fileID);

        x(n+1:2*n) = 0;
        fprintf('func_num = %d\n', func_num);
        for k = 1:1
            f = cec22_test_func(x(1:n), func_num);
            for j = 1:1
                fprintf('f%d(x[%d]) = %.10f,\n', func_num, j, f(j));

                FileName = sprintf('test_data/current_result_%d.txt', func_num);
                fileID = fopen(FileName, 'w+');
                if fileID == -1
                    error('Error: Cannot open input file for reading');
                end
                fprintf(fileID, 'f%d(x[%d]) = %.10f,\n', func_num, j, f(j));
                fclose(fileID);
            end
        end
    end
end