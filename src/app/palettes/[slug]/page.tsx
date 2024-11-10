/* eslint-disable @typescript-eslint/no-explicit-any */
import { Button } from "@/components/ui/button";
import { sql } from "@vercel/postgres";
import dayjs from "dayjs";
import relativeTime from "dayjs/plugin/relativeTime";
import "dayjs/locale/en"; // Load English locale
import Link from "next/link";
import NotFound from "@/app/not-found";
import InsertLikes from "@/components/insertLikes";

// Add support for relative time comparisons
dayjs.extend(relativeTime);

export default async function Page({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const slug = (await params).slug;

  const colorsName = [`red`, `green`, `blue`, `cyan`, `yellow`];

  // تحقق من طول الـ slug للتأكد أنه يتوافق مع الحد الأدنى
  if (slug.length <= 10) {
    // استعلام يجلب بيانات المجموعات التي تحتوي على الـ slug ضمن `tags`
    const { rows: tagg } = await sql`
  SELECT 
    cp.id, cp.color1, cp.color2, cp.color3, cp.color4, cp.created_at, 
    COALESCE(l.likes_count, 0) AS likes_count  -- يستخدم COALESCE لضمان عدم وجود قيمة فارغة
  FROM color_palettes cp
  LEFT JOIN likes l ON cp.id = l.id  -- يربط بين الجداول باستخدام العمود id من likes
  WHERE ${slug} = ANY(cp.tags)
    `;
    if (tagg.length === 0) {
      return <NotFound />;
    }
    return (
      <section className="w-full flex flex-col justify-center items-center">
        <div className="w-full h-full">
          <div className="grid grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 animate-out gap-5">
            {tagg.map(
              ({
                id,
                color1,
                color2,
                color3,
                color4,
                created_at,
                likes_count,
              }: any) => (
                <div
                  key={id}
                  className={`flex flex-col justify-center items-center`}
                >
                  <Link
                    href={`/palettes/` + id}
                    className="w-full h-20 rounded-tl-xl rounded-tr-xl"
                    style={{ backgroundColor: `#${color1}` }}
                  ></Link>
                  <Link
                    href={`/palettes/` + id}
                    className="w-full h-14"
                    style={{ backgroundColor: `#${color2}` }}
                  ></Link>
                  <Link
                    href={`/palettes/` + id}
                    className="w-full h-10"
                    style={{ backgroundColor: `#${color3}` }}
                  ></Link>
                  <Link
                    href={`/palettes/` + id}
                    className="w-full h-10 rounded-bl-xl rounded-br-xl"
                    style={{ backgroundColor: `#${color4}` }}
                  ></Link>
                  <div className="w-full flex justify-between items-center py-3">
                    <InsertLikes
                      id={color1 + color2 + color3 + color4}
                      likes_count={`${likes_count}`}
                      color1={color1}
                      color2={color2}
                      color3={color3}
                      color4={color4}
                    />
                    <h4 className="text-xs font-normal opacity-80">
                      {dayjs(created_at).locale("ar").fromNow()}
                    </h4>
                  </div>
                </div>
              )
            )}
          </div>
        </div>
      </section>
    );
  }

  const { rows } = await sql`
    WITH palette_data AS (
      SELECT * FROM color_palettes WHERE id = ${slug}
    ),
    like_data AS (
      SELECT likes_count FROM likes WHERE id = ${slug}
    ),
    tagged_palettes AS (
      SELECT * FROM color_palettes WHERE ${slug} = ANY(tags)
    )
    SELECT 
      pd.color1, pd.color2, pd.color3, pd.color4, pd.created_at, pd.tags, 
      ld.likes_count,
      tp.id AS tagged_id, tp.color1 AS tagged_color1, tp.color2 AS tagged_color2, tp.color3 AS tagged_color3, tp.color4 AS tagged_color4
    FROM palette_data pd
    LEFT JOIN like_data ld ON pd.id = ${slug}
    LEFT JOIN tagged_palettes tp ON TRUE
  `;

  const palette = rows[0]; // Assuming there's at least one row
  const { likes_count, color1, color2, color3, color4, created_at, tags } =
    palette;

  const distance = dayjs(created_at).locale("en").fromNow();

  return (
    <section className="w-full">
      <div className="w-full h-full flex justify-center items-center">
        <div className="w-full flex flex-col justify-center items-center px-16 pt-7 max-w-[72vh]">
          <div
            className={`w-full h-56 rounded-tl-xl rounded-tr-xl`}
            style={{ backgroundColor: `#${color1}` }}
          ></div>
          <div
            className={`w-full h-32`}
            style={{ backgroundColor: `#${color2}` }}
          ></div>
          <div
            className={`w-full h-20`}
            style={{ backgroundColor: `#${color3}` }}
          ></div>
          <div
            className={`w-full h-20 rounded-bl-xl rounded-br-xl`}
            style={{ backgroundColor: `#${color4}` }}
          ></div>
          <div className="w-full flex justify-between items-center py-4">
            <div className="flex gap-3">
              <InsertLikes
                id={color1 + color2 + color3 + color4}
                likes_count={`${likes_count}`}
                color1={color1}
                color2={color2}
                color3={color3}
                color4={color4}
              />
              <Button variant={"outline"} size={"default"}>
                Image
              </Button>
              <Button variant={"outline"} size={"default"}>
                Link
              </Button>
            </div>
            <h4 className="text-sm font-normal opacity-80">{distance}</h4>
          </div>
        </div>
      </div>

      <div className="w-full flex justify-center items-center gap-3 px-16">
        {tags.map((tag: string, index: number) => (
          <Link
            href={`/palettes/` + tag}
            key={index}
            className="border p-1 px-3 rounded-full flex justify-center items-center gap-2"
          >
            {colorsName.includes(tag) ? ( // تحقق مما إذا كان tag في قائمة الألوان
              <div
                className="w-4 h-4 rounded-full"
                style={{ backgroundColor: tag }}
              ></div>
            ) : null}
            <p>{tag}</p>
          </Link>
        ))}
      </div>

      <div>
        {rows.map(({ id, color1, color2, color3, color4 }) => (
          <section
            key={id + Date.now().toString()}
            className={`border p-1 px-3 flex flex-col justify-center items-center`}
          >
            <div className="w-full h-full flex justify-center items-center">
              <div className="w-full flex flex-col justify-center items-center px-16 pt-7 max-w-[72vh]">
                <div
                  className="w-full h-10"
                  style={{ backgroundColor: `#${color1}` }}
                ></div>
                <div
                  className="w-full h-10"
                  style={{ backgroundColor: `#${color2}` }}
                ></div>
                <div
                  className="w-full h-10"
                  style={{ backgroundColor: `#${color3}` }}
                ></div>
                <div
                  className="w-full h-10"
                  style={{ backgroundColor: `#${color4}` }}
                ></div>
              </div>
            </div>
          </section>
        ))}
      </div>
    </section>
  );
}
