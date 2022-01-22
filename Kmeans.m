m=3;disp('Clustering in 3D plane');
disp('sample input :[1 0 10;0 1 5]');
xyz=input('3D matrix: ');
% xyz=[8.5 80 40; 7 90 80; 9.5 95 80; 7.8 75 30; 8.7 83 20; 9.8 89 10];
sz1=size(xyz);
sz=sz1(1,1);
a=normalize(xyz,'Range');
x=input('no of clusters: ');
if(x>size(a))
  x=input('enter valid number of cluster: ');
end
b=5;
c=abs (floor(sz(1,1)/x));
for i=1:x
    add=c*i;
    for j=1:m
       centre(i,j)=a(add,j);
    end
end
for g=1:b-1
for i=1:sz(1,1)
    for j=1:x
      dist(i,j)=abs(a(i,1)-centre(j,1))+abs(a(i,2)-centre(j,2))+abs(a(i,3)-centre(j,3));
      dbstop if error
    end
end
   for i=1:sz(1,1)
      small=dist(i,1);
      dist(i,x+1)= 1;
      for j=1:x
          if(dist(i,j)< small)
              small=dist(i,j);
              dist(i,x+1)= j;
          end
      end
   end
   
   
   for j=1:x
        ind(j)=0;
end
for i=1:sz(1,1)
    for j=1:x
        if(dist(i,x+1)==j)
         ind(j)=ind(j)+1;
         x1(j,ind(j))=a(i,1);
         y1(j,ind(j))=a(i,2);
         z1(j,ind(j))=a(i,3);
         labl(j,ind(j))=i;
   
        end
     end
end
for i=1:x
  sumx=0;
  sumy=0;
  sumz=0;
  for j=1:ind(i)
     xp(j)=x1(i,j);
     yp(j)=y1(i,j);
     zp(j)=z1(i,j);
     lp(j)=labl(i,j);
     sumx=sumx+x1(i,j);
     sumy=sumy+y1(i,j);
     sumz=sumz+z1(i,j);
  end
   centre(i,1)= sumx/ind(i);
   centre(i,2)= sumy/ind(i);
     clear xp;
     clear yp;
     clear zp;
     clear lp;
end
end

for i=1:sz(1,1)
    for j=1:x
      dist(i,j)=abs(a(i,1)-centre(j,1))+abs(a(i,2)-centre(j,2))+abs(a(i,3)-centre(j,3));
    end
end
for i=1:sz(1,1)
      small=dist(i,1);
      dist(i,x+1)= 1;
      for j=1:x
          if(dist(i,j)< small)
              small=dist(i,j);
              dist(i,x+1)= j;
          end
      end
end
for j=1:x
        ind(j)=0;
end
for i=1:sz(1,1)
    for j=1:x
        if(dist(i,x+1)==j)
         ind(j)=ind(j)+1;
         x1(j,ind(j))=a(i,1);
         y1(j,ind(j))=a(i,2);
         z1(i,ind(j))=a(i,3);
         labl(j,ind(j))=i;
        end
     end
end

for i=1:x
  sumx=0;
  sumy=0;
  sumz=0;
  for j=1:ind(i)
     xp(j)=x1(i,j);
     yp(j)=y1(i,j);
     zp(j)=z1(i,j);
     lp(j)=labl(i,j);
     sumx=sumx+x1(i,j);
     sumy=sumy+y1(i,j);
     sumz=sumz+z1(i,j);
  end
   centre(i,1)= sumx/ind(i);
   centre(i,2)= sumy/ind(i);
   scatter3(xp,yp,zp,'filled'); 
   title('K means clustering (Student Relative grading)(Label shows roll number)');
   xlabel('Curricular');
   ylabel('Attendance');
   zlabel('Co-curricular');
   %to print label
     ltrans=lp';
     bj = num2str(ltrans); l = cellstr(bj);
     dx = 0.02; dy = 0.02;dz = 0.02; %displacement so the text does not overlay the data points
     text(xp+dx, yp+dy,zp+dz,l);
     hold on;
     clear xp;
     clear yp;
     clear zp;
     clear lp;
end
