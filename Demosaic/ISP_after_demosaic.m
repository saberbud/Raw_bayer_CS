function [image] = ISP_after_demosaic(dm_scaled)

%% Step 7: color correction (tune mapping)
srgbMatrix= [0.66433,	-0.03331,	-0.03603;
0.08503,	0.77001,	0.06621;
-0.134,	-0.06281,	0.74561];

   
ccdm=double(dm_scaled);
[r c wl] = size(ccdm);
ccdm_rs=reshape(ccdm,[r*c wl]);
ccdm_corr=(srgbMatrix'*ccdm_rs');
cout=reshape(ccdm_corr',[r c wl]);

%% Step 8: gamma correction
final = lin2rgb(cout,'OutputType','uint8','ColorSpace','sRGB'); %%%%%%%%%%% Best matching with sRGB standard

image = final;

end
