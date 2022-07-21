%% 
clear all;
I=imread('L:\Developer\JagdStandard\MATLAB\test_7_21\a.jpg');
[W,H,nChanels]=size(I);

degree=15;
eddy_mat=zeros(W,H,nChanels);
swirl_degree=degree./1000;
midX=W/2;
midY=H/2;

for y=1:H
    for x=1:W
        Yoffset=y-midY;
        Xoffset=x-midX;
        
        radian=atan2(Yoffset,Xoffset);
        radius=sqrt(Xoffset^2+Yoffset^2);
        X=int32(radius*cos(radian+radius*swirl_degree)+midX);
        Y=int32(radius*sin(radian+radius*swirl_degree)+midY);
        
        X(X>W)=W;Y(Y>H)=H;
        X(X<1)=1;Y(Y<1)=1;
        eddy_mat(x,y,:)=I(X,Y,:);
    end
end
eddy_mat=uint8(eddy_mat);
disp('已完成图像旋转...'),pause(0.5)

%T=affine2d([1 0 0;0 1 0;0 0 1]);
%dst_mat=imwarp(eddy_mat,T);
imshow(eddy_mat)


map_mat=rgb2gray(eddy_mat);
disp('已获得映射矩阵...'),pause(0.5)
imshow(map_mat)

[Xmesh,Ymesh]=meshgrid(1:H,1:W);
surf(Xmesh,map_mat,Ymesh,'EdgeColor','none','LineWidth',0.01,'CData',eddy_mat,'FaceColor','interp')
disp('已构造曲面...'),pause(0.5)

axes=gca;
axes.PlotBoxAspectRatio=[0.6860    0.6875    1.0000];
axes.CameraPosition=[-0.9862    2.2773    1.5062].*1e3;
axes.Color=[0 0 0];
disp('已调整曲面角度')

end
%%