#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

struct TRIE
{
	int index;
	struct TRIE *next[256];
};

struct NEXT
{
	unsigned index;
	unsigned next;
};

void assignTrie(struct TRIE *t,unsigned char* word,int index)
{
	if(word[0]=='\0')
	{
		t->index=index;
		return;
	}
	if(t->next[word[0]]==NULL)
	{
		t->next[word[0]] = malloc(sizeof(struct TRIE));
		for(int i=0;i<256;i++)t->next[word[0]]->next[i]=NULL;
		t->next[word[0]]->index=-1;
	}
	assignTrie(t->next[word[0]],word+1,index);
	return;
}
				

int main()
{
	//read dic
	int index,cost[115828];
	unsigned char *dic[115828][4],ch,tmp[64];
	struct TRIE root;
	for(int i=0;i<256;i++)root.next[i]=NULL;
	FILE *fp = fopen("../dic/jdic.txt","r");
	for(int i=0;i<115828;i++)
	{
		for(int j=0;j<4;j++)
		{
			index=0;
			while(true)
			{
				ch = fgetc(fp);
				if(ch==' ')break;
				tmp[index]=ch;
				index++;
			}
			tmp[index]='\0';
			dic[i][j]=malloc(index+2);
			strcpy(dic[i][j],tmp);
			while(fgetc(fp)!=' ');
		}
		//trie
		assignTrie(&root,dic[i][0],i);
		//cost
		//before '.'
		index=0;
		while(true)
		{
			ch = fgetc(fp);
			tmp[index]=ch;
			if(ch=='.')break;
			index++;
		}
		cost[i]=atoi(tmp)*100000;
		//after '.'
		index=10000;
		while(true)
		{
			ch = fgetc(fp);
			if(ch=='\n')break;
			cost[i] += ((int)(ch-'0'))*index;
			index/=10;
		}
	}
	fclose(fp);

	//perse with dic
	unsigned char sen[512],word[512];
	int	len,left,right;
	int min_index[512],min_i[512],bp[512];
	unsigned long min_cost[512];
	struct TRIE *t;
	min_cost[0]=0;
	while ((sen[0] = getchar()) != (unsigned char)EOF)
	{
		//get sentence
		for(int i=1;i<512;i++)sen[i]=0;
		len=1;
		while((sen[len] = getchar()) != '\n')len++;
		sen[len]=0;
		for(int i=1;i<512;i++)min_cost[i]=100000000000;
		//search
		left=0;right=len;
		for(;left<right;left+=2)
		{
			if(min_cost[left]==100000000000)continue;
			t=&root;
			for(int i=left;i<right;i++)
			{
				if(t->next[sen[i]]==NULL)
					break;
				t=t->next[sen[i]];
				if(t->index!=-1)
				{
					if(min_cost[i+1]>min_cost[left]+cost[t->index])
					{
						index=t->index;
						min_index[i+1]=index;
						min_cost[i+1]=min_cost[left]+cost[index];
						min_i[i+1]=left;
					}
				}
			}
		}

		index=512;
		while(right!=0)
		{
			index--;
			bp[index]=min_index[right];
			right=min_i[right];
		}
		for(int i=index;i<512;i++)
		{
			printf("%s\t",dic[bp[i]][0]);
			int pos=0;
			while(pos<8 && dic[bp[i]][3][pos]!='-')printf("%c",dic[bp[i]][3][pos++]);
			printf("\n");
		}
		printf("EOS\n");
	}
	for(int i=0;i<115828;i++)
	for(int j=0;j<4;j++)
		free(dic[i][j]);
	return 0;
}
