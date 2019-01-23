close all; clear all;

%input_filename='./image_orig.h5';
%output_name='./DM_orig.h5';

%input_filename='./image_884_rec_CI.h5';
%output_name='./DM_884_rec_CI.h5';

%input_filename='./image_16164_rec_CI.h5';
%output_name='./DM_16164_rec_CI.h5';

%input_filename='./image_32324_rec_CI.h5';
%output_name='./DM_32324_rec_CI.h5';

input_filename='./image_884_rec_dbl_SF_JPEG85.h5';
output_name='./DM_884_rec_CI_JP85.h5';

raw=h5read(input_filename,'/data');

raw_bayer = squeeze(raw);
pattern='bggr';
%pattern='rggb';
output_tmp = ISP_until_demosaic(raw_bayer,pattern);
output = ISP_after_demosaic(output_tmp);

%output_transfer = rot90(output,2); %For 1, 2, comment out if running 3
output_transfer = output; % For 3, comment out if running 1, 2

DM = permute(output_transfer,[3,2,1]);
DM = double(DM)/255.0;

shape = size(DM);

h5create(output_name,'/data',[shape]);
h5write(output_name,'/data',DM);
















