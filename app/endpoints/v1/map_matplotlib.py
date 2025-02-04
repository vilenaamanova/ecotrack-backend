from fastapi.responses import HTMLResponse
from app.services.waterquality import WaterqualityServiceDep
from fastapi import APIRouter

router = APIRouter(tags=['mapWaterquality'])

import base64
from io import BytesIO
import matplotlib.pyplot as plt

def create_pie_chart(ph, do, nitrates, phosphates):
    # Данные для круговой диаграммы
    labels = ['pH', 'DO', 'Nitrates', 'Phosphates']
    sizes = [ph, do, nitrates, phosphates]
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

    # Создаем круговую диаграмму
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Чтобы диаграмма была круглой

    # Сохраняем диаграмму в байтовый поток
    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)

    # Кодируем изображение в base64
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    return image_base64

import folium
from fastapi.responses import HTMLResponse

@router.get('/waterquality/map/', response_class=HTMLResponse)
async def get_waterquality_map(
    waterquality_service: WaterqualityServiceDep,
):
    # Получаем данные о качестве воды
    waterquality_data = await waterquality_service.read_many()

    # Создаем карту с центром на первом объекте
    if waterquality_data:
        first_point = waterquality_data[0]
        m = folium.Map(location=[first_point.latitude, first_point.longitude], zoom_start=10)
    else:
        m = folium.Map(location=[0, 0], zoom_start=2)

    # Добавляем маркеры с круговыми диаграммами
    for data in waterquality_data:
        # Генерируем круговую диаграмму
        pie_chart_image = create_pie_chart(data.ph, data.do, data.nitrates, data.phosphates)

        # Создаем HTML для попапа с диаграммой
        popup_html = f"""
        <div>
            <h4>{data.model}</h4>
            <img src="data:image/png;base64,{pie_chart_image}" alt="Pie Chart">
            <p>pH: {data.ph}</p>
            <p>DO: {data.do}</p>
            <p>Nitrates: {data.nitrates}</p>
            <p>Phosphates: {data.phosphates}</p>
        </div>
        """

        # Добавляем маркер на карту
        folium.Marker(
            location=[data.latitude, data.longitude],
            popup=folium.Popup(popup_html, max_width=300),
            tooltip=data.model,
        ).add_to(m)

    # Возвращаем HTML-код карты
    return m._repr_html_()