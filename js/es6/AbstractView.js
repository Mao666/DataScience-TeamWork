/**
 * 该类是视图的抽象类. ListView , GridView继承该类.
 */
class AbstractView{
    /**
     * 构造器.
     * @param Pagination pagination. Pagination类型，pagination对象
     * @param object options, 视图选项
     */
    constructor(pagination, options){
        this.settings = $.extend({
            listContainer:      '#itemlist',
            mapContainer:      '#mapContainer',
            modalContainer:     '#modalContainer',
            pagerCountainer:    '.pager',
            totalCount:         '.total .count'
        }, options||{});
        this.pagination = pagination;
        this.name = 'abstract';
    }

    /**
     * 抽象方法
     */
    init(){}

    /**
     * 返回没有数据时显示的信息.
     * @returns {string}
     */
    static get noSearchData(){
        return `<li class="no-data">no data！</li>`;
    }

    /**
     * 以modal窗口显示详细信息.
     * @param model, 产品对象
     */
    detail(model){
        var self = this;
        $(self.settings.modalContainer).empty().append(
            `
<div class="modal fade bs-example-modal-lg" tabindex="-1" role="dialog" id="mymodal" >
  <div class="modal-dialog modal-lg" role="document">
    <div class="modal-content" >
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <h4 class="modal-title">${model.Car_Series}</h4>
      </div>
      <div class="modal-body">

       <div class="row">  
             <div class="col-md-4">
                 <img src="${model.img}" style="width:280px;height:171px"class="center-block">
                
             </div>          
             <div class="col-md-4 text-left">
             <p></p>

                <p><strong>Series:</strong><span>  ${model.Car_Series}</span></p>
                <p><strong>Style Name:</strong><span>  ${model.Style_Name}</span></p>
                <p><strong>Body Style:</strong><span>  ${model.Body_Style}</span></p>
                <p><strong>Car Type:</strong><span>  ${model.Car_Type}</span></p>
                <p><strong>Drivetrain:</strong><span>  ${model.Drivetrain}</span></p>
                <div style="width:100%;height:1px;background-color:#f0f0f0"></div>          
             </div>  

             <div class="col-md-4 text-left" >
                <p></p>
                <p><strong>Base Curb Weight:</strong><span>  ${model.Base_Curb_Weight}</span></p>
                <p><strong>Length:</strong><span>  ${model.Length}</span></p>
                <p><strong>Width:</strong><span>  ${model.Width}</span></p>
                <p><strong>Height:</strong><span>  ${model.Height}</span></p>
                <p><strong>Wheelbase:</strong> ${model.Wheelbase}</span></p>                             
                <div style="width:100%;height:1px;background-color:#f0f0f0"></div> 
             </div>                
         </div>
         <div class="row"> 
             <div class="col-md-8">
                <div class="center-block" id="figure"></div>
             </div> 
             <div class="col-md-4">
                 
             </div> 
         </div>

         <div class="row">  
             <div class="col-md-4 text-center" style="padding-top:40px">
             <h2><strong>Score:</strong><span style="color:#ffc21f"> ${model.Final_Score_Safe}</span></h2> 
             </div>          
             <div class="col-md-4 text-left">
             <p></p>

                <p><strong>Horsepower:</strong><span>  ${model.Horsepower}</span></p>
                <p><strong>Engine:</strong><span>  ${model.Engine}</span></p>
                <p><strong>PassengerCapacity:</strong><span>  ${model.Passenger_Capacity}</span></p>
                <p><strong>Passenger Doors:</strong><span>  ${model.Passenger_Doors}</span></p>                    
             </div>  

             <div class="col-md-4 text-left" >
                <p></p>
                <p><strong>Accident Rate:</strong><span>  ${model.Accident_Rate}</span></p>
                <p><strong>Death Rate:</strong><span>  ${model.Death_Rate}</span></p>
                <p><strong>Safety Score:</strong><span>  ${model.Safety_Score}</span></p>
                <p><strong>Overall Score:</strong><span>  ${model.Overall_Score}</span></p>
                                            
               
             </div>                
         </div>


         <div class="row"> 
             <div class="col-md-12" style="margin-top:80px;padding-left:20px">
                 <div class="center-block" id="echart" style="height:600px;width:800px"></div>
             </div> 
    
         </div>



      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal"style="background-color: #ffc21f;border-color:#ffc21f">Close</button>
      
      </div>
    </div><!-- /.modal-content -->
  </div><!-- /.modal-dialog -->
</div><!-- /.modal -->

            `
        );
        $('#mymodal').modal('show')


        var myChart = echarts.init(document.getElementById('echart'));
var weatherIcons = {
    '': '',
    '': '',
    '': ''
};

var seriesLabel = {
    normal: {
        show: true,
        textBorderColor: '#333',
        textBorderWidth: 2
    }
}

        // 指定图表的配置项和数据
        var option = {
    title: {
        text: 'model compare'
    },
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'shadow'
        }
    },
    legend: {
        data: ['max', 'average', 'this']
    },
    grid: {
        left: 100
    },
    toolbox: {
        show: true,
        feature: {
            saveAsImage: {}
        }
    },
    xAxis: {
        type: 'value',
        name: '',
        axisLabel: {
            formatter: '{value}'
        }
    },
    yAxis: {
        type: 'category',
        inverse: true,
        data: ['Accident Rate', 'Death Rate', 'Safety Score'],
        axisLabel: {
            formatter: function (value) {
                return '{' + value + '| }\n{value|' + value + '}';
            },
            margin: 20,
            rich: {
                value: {
                    lineHeight: 30,
                    align: 'center'
                },
                Sunny: {
                    height: 40,
                    align: 'center',
                    backgroundColor: {
                        image: weatherIcons.Sunny
                    }
                },
                Cloudy: {
                    height: 40,
                    align: 'center',
                    backgroundColor: {
                        image: weatherIcons.Cloudy
                    }
                },
                Showers: {
                    height: 40,
                    align: 'center',
                    backgroundColor: {
                        image: weatherIcons.Showers
                    }
                }
            }
        }
    },
    series: [
        {
            name: 'max',
            type: 'bar',
            data: [165, 140, 143],
            label: seriesLabel,
            markPoint: {
                symbolSize: 1,
                symbolOffset: [0, '50%'],
                label: {
                   normal: {
                        formatter: '{a|{a}\n}{b|{b} }{c|{c}}',
                        backgroundColor: 'rgb(242,242,242)',
                        borderColor: '#aaa',
                        borderWidth: 1,
                        borderRadius: 4,
                        padding: [4, 10],
                        lineHeight: 26,
                        // shadowBlur: 5,
                        // shadowColor: '#000',
                        // shadowOffsetX: 0,
                        // shadowOffsetY: 1,
                        position: 'right',
                        distance: 20,
                        rich: {
                            a: {
                                align: 'center',
                                color: '#fff',
                                fontSize: 18,
                                textShadowBlur: 2,
                                textShadowColor: '#000',
                                textShadowOffsetX: 0,
                                textShadowOffsetY: 1,
                                textBorderColor: '#333',
                                textBorderWidth: 2
                            },
                            b: {
                                 color: '#333'
                            },
                            c: {
                                color: '#ff8811',
                                textBorderColor: '#000',
                                textBorderWidth: 1,
                                fontSize: 22
                            }
                        }
                   }
                },
                data: [
                    {type: 'max', name: 'max: '},
                    {type: 'this', name: 'this: '}
                ]
            }
        },
        {
            name: 'average',
            type: 'bar',
            label: seriesLabel,
            data: [145, 135, 110]
        },
        {
            name: 'this',
            type: 'bar',
            label: seriesLabel,
            data: [155, 136, 130]
        }
    ]
};

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);



}
    
    /**
     * 显示一共找到多少条满足条件
     */
    displayTotalCount(){
        console.log('this.pagination.totalCount:',this.pagination.totalCount);
        $(this.settings.totalCount).text(this.pagination.totalCount);
    }

    /**
     * 显示翻页按钮
     */
    displayPager(){
        var $pages = this._pageButtons();
        $(this.settings.pagerCountainer).empty().append($pages);
    }

    _pageButtons(){
        var $container = $('<div>').addClass('ui pagination menu');
        var pagerange = this.pagination.pageRange;
        for(var i = pagerange[0]; i <= pagerange[1]; i++){
            var $btn = $('<a>').addClass('item').text(i+1);
            if(i == this.pagination.page){
                $btn.addClass('active').css("background-color","#ffc21f");;
            }
            $container.append($btn);
        }
        return $container;
    }

    /**
     * 删除前一页内容, 显示当前页内容.
     * @param array items 当前页的数组对象.
     */
    replaceProducts(items){
        var self = this;
        $(self.settings.listContainer).empty().removeAttr('style');
        var htmlString = this._models2HtmlStr(items);
        if(htmlString)
            $(self.settings.listContainer).html(htmlString);
        else{
            $(self.settings.listContainer).html(this.constructor.noSearchData);
        }
       // window.scrollTo(0,0);
    }
    /**
     * 保持前一页内容, 在前页内容的后面继续添加当前页的内容
     * @param array items 当前页的数组对象.
     */
    appendProducts(items){
        var self = this;
        var htmlString = this._models2HtmlStr(items);
        if(htmlString)
            $(self.settings.listContainer).append(htmlString);
    }

    /**
     * public方法, 该方法调用displayTotalCount(),appendProducts(),和displayPager().
     * @param items 当前页的数组对象.
     * @param append 默认保留前一页内容, 在前一页后面继续添加当前页内容
     */
    display(items, append=true){
        $(this.settings.mapContainer).empty().removeAttr('style');
        this.displayTotalCount();
        if(append){
            this.appendProducts(items);
        }else{
            this.replaceProducts(items);
        }
        this.displayPager();
    }

    /**
     * 抽象方法.根据当前页数组对象返回html字符串.
     * @param array models 当前页的数组对象.
     * @private
     */
    _models2HtmlStr(models){

    }
}