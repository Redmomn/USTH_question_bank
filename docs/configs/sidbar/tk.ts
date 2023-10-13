import type { SidebarConfig } from '@vuepress/theme-default'

export const sidebarTk: SidebarConfig = {
    '/tiku/':[
        {
            text:'test',
            children:[
                '单选.md',
                '多选.md',
                '判断.md'
            ]
        }
    ]
}