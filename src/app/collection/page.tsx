"use client";
/* eslint-disable @typescript-eslint/no-explicit-any */
import InsertLikes from "@/components/insertLikes";
import Link from "next/link";
import dayjs from "dayjs";
import relativeTime from "dayjs/plugin/relativeTime";
import { usePalettes } from "@/components/UsernameContext";
dayjs.extend(relativeTime);

export default function Collection() {
  const { palettes } = usePalettes();

  return (
    <div className="w-full h-full">
      <div className="grid grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 animate-out gap-5">
        {palettes.map(
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
  );
}
