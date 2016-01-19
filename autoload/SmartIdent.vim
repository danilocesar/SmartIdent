let s:script_folder_path = escape( expand( '<sfile>:p:h' ), '\' )
if has('python')
    " Python 2
    py import sys
    py import vim
    exe 'python sys.path = sys.path + ["' . s:script_folder_path . '/../python"]'
    "py import smartident_vim
else
    " Python 3
    py3 import sys
    py3 import vim
    exe 'python3 sys.path = sys.path + ["' . s:script_folder_path . '/../python"]'
    "py3 import smartident_vim
endif

function! SmartIdent#Setup()
    " When vim is in diff mode, don't run
   if &diff
     return
   endif

   augroup smartident
       autocmd BufReadPre,FileReadPre,FileType * call SmartIdent()

       call SmartIdent()
   augroup END

endfunction
