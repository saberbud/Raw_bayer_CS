function [image] = ISP_until_demosaic(raw_bayer,pattern)
%ISP 
%% step 1: read raw data
raw_bayer = uint16(raw_bayer*(2^14-1));
raw_bayer = raw_bayer';

%% Step 2: Black level correction & offset
black_level = 50; %Camera dependent
raw_bayer_rs_10bit = raw_bayer/2^4-black_level; % Correct: 14-bit --> 10-bit

%% Step 3: white balance correction: so that the average color is gray
wb=[2 1;1 1.5]; 
rawwb = zeros(size(raw_bayer_rs_10bit));
for ii=1:2
    for jj=1:2
        rawwb(ii:2:end,jj:2:end)=raw_bayer_rs_10bit(ii:2:end,jj:2:end).*squeeze(wb(ii,jj));
    end
end
%% Step 4: demosaicing: reconstruct a full color image from Bayer filtered mosaiced data
raw_bayer_16bit = uint16(rawwb*2^6);
dm = demosaic(raw_bayer_16bit,pattern);
dm_scaled=double(dm)/2^16;


image = dm_scaled;

end
