% rebase('base.tpl', title='Page Title')
<ul>
% for name in names:
    <li>{{name}}</li>
% end
</ul>