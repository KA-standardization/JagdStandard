# 配置

```
" Vim Plugin
call plug#begin('~/.vim/plugged')
Plug 'morhetz/gruvbox'
Plug 'preservim/nerdtree'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'easymotion/vim-easymotion'
Plug 'preservim/nerdcommenter'
" Plug 'Yggdroot/LeaderF', { 'do': ':LeaderfInstallCExtension' }
call plug#end()

let mapleader = ";"
nnoremap <Leader>q :q<CR>
nnoremap <Leader>w :w<CR>
nnoremap <Leader>g :NERDTreeToggle<CR>
nnoremap <Leader>f :NERDTreeFind<CR>
nnoremap <Leader>h ^
nnoremap <Leader>l $
nnoremap <C-g> :set nohlsearch<CR>
nnoremap <C-i> :set ignorecase<CR>

set clipboard=unnamedplus    " 使用系统剪切版 -> Vim
set clipboard=unnamed      " Vim -> 系统剪切版
set hlsearch
set cursorline
set undofile
set history=1000
set relativenumber
set nu
set expandtab
set tabstop=4
set softtabstop=4
set shiftwidth=4
" colorscheme gruvbox
autocmd vimenter * nested colorscheme gruvbox
set bg=dark

let g:EasyMotion_smartcase = 1
nmap f <Plug>(easymotion-s)

let g:NERDSpaceDelims = 1
```

# 命令

| 命令                              | Desc                               | Ex.               |
| --------------------------------- | ---------------------------------- | ----------------- |
| :vs filename                      | 横向分割显示                       |                   |
| :sp filename                      | 纵向分割显示                       |                   |
| :only                             | 关闭除光标所在的窗口之外的其他窗口 |                   |
| C-v                               | visual-block                       |                   |
| v                                 | visual                             |                   |
| V                                 | visual-line                        |                   |
| :%s/oldWord/newWord/g             | 全局直接替换                       | :1,3s/aaa/bbb/g   |
| :%s/oldWord/newWord/gc            | 全局询问替换                       |                   |
| q->宏名->执行命令->Esc->q         | 宏                                 |                   |
| :register 宏名                    | 查看宏                             |                   |
| @宏名                             | 执行宏                             |                   |
| :let @宏名 = ""                   | 删除宏                             |                   |
| "->寄存器名->y     "->寄存器名->p | 寄存器                             |                   |
| :tabe :tabedit                    | 窗口标签                           | :tabedit filename |
| :tabp                             | 上一个窗口                         |                   |
| :tabn                             | 下一个窗口                         |                   |
| ynw yy y$                         |                                    |                   |
| p P                               |                                    |                   |
| dnd dd                            |                                    |                   |
| vit                               | 复制标签中的数据                   | \<a\>aaaaa\</a\>  |
| vi"                               | 复制到末尾引号"                    | "aaaaaaaa bbbbb"  |

# tmp

```
进入常规模式；将光标移动到第一行的第一个字母上；执行qa命令，开始录制宏a；执行gUl命令，将首字母转换为大写；执行w命令，移动到下一单词；执行cw命令，修改单词；输入“was”；点击Esc键，返回常规模式；执行A命令，在行尾添加文字；输入“in Akbar's court”；点击Esc键，返回常规模式；执行q命令，完成录制宏；

寄存器，分为有名寄存器和无名寄存器
默认情况下操作的数据，数据被提取至无名寄存器暂存，从无名寄存器粘贴
提取的操作：y yank、yy、x、dd
粘贴的操作：p、P

在.vimrc里面的配置 set clipboard=unnamed，其实就是将系统剪切板的数据放入vim的无名寄存器
- 在vim内粘贴后
- 在浏览器粘贴，对比

寄存器的使用方式，通过在操作寄存器之前使用英文的引号键来触发( " ), 在引号后跟上寄存器的名称，一般可使用a-z的小写字母，
举例：
7890

- 复制过程
 1. 光标移动至行首，按键v e，来选中要复制的内容
 2. 按键：英文的引号( " )，触发寄存器声明
 3. 按键：z，标记使用寄存器名称为z
 4. 按键：y，将选中的内容提取至z寄存器
- 粘贴过程
 1. 光标移动至想粘贴的地方
 2. 按键：英文的引号( " )，触发寄存器声明
 3. 按键：z，标记使用寄存器名称为z
 4. 按键：p，粘贴z寄存器内容至光标处

vimgolf.com

JetBrains/Ideavim

C o C i outfile infile
```

